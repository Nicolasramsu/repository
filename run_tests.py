import unittest
import logging
import json
import sys

def load_config(file_path):
    """Loads configuration from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Configuration file not found.")
        sys.exit(1)

def run_tests(config):
    """Runs automatic tests and saves the results in a log file."""
    # Set up logging
    logging.basicConfig(filename=config["test_log_file"], level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Discover and run tests
    try:
        test_suite = unittest.defaultTestLoader.discover('tests')
        test_runner = unittest.TextTestRunner()
        test_results = test_runner.run(test_suite)
        
        # Log test results
        if test_results.wasSuccessful():
            logging.info("All tests passed successfully.")
        else:
            logging.error("Some tests failed.")
    except Exception as e:
        logging.error(f"Error running tests: {e}")

if __name__ == "__main__":
    config_file = "config.json"
    config = load_config(config_file)
    run_tests(config)