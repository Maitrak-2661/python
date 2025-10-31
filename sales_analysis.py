import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:
    def __init__(self):
        self.data = None # Initialize the DataFrame
        print("SalesDataAnalyzer initialized.")

    def load_data(self, file_path):
        try:
            # TODO: Load the CSV file into self.data and handle exceptions.
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
            return True
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return False
        except pd.errors.EmptyDataError:
             print("Error: The file is empty.")
             return False
        # Add more exceptions as needed...

    def explore_data(self):
        if self.data is not None:
            # TODO: Implement methods like head(), info(), describe().
            print("\n--- First 5 Rows ---")
            print(self.data.head())
            print("\n--- Basic Info ---")
            self.data.info()
        else:
            print("No data loaded. Please load a dataset first.")

    # ... other methods like clean_data, visualize_data, etc.


def display_main_menu():
    print("\n======== Data Analysis & Visualization Program ========")
    print("1. Load Dataset")
    print("2. Explore Data")
    print("3. Perform DataFrame Operations")
    print("4. Handle Missing Data")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    print("=====================================================")

def main():
    analyzer = SalesDataAnalyzer()
    
    while True:
        display_main_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            file_path = input("Enter the path of the dataset (CSV file): ")
            analyzer.load_data(file_path)
        elif choice == '2':
            analyzer.explore_data()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        # TODO: Implement all other menu options by calling analyzer methods

if __name__ == "__main__":
    main()