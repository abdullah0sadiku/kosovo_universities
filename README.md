# Kosovo Universities Information System GUI

## Overview

This is a Python-based Graphical User Interface (GUI) application designed to provide comprehensive information about universities, faculties, and departments in Kosovo. The application allows users to explore academic programs, view statistics, and export data in a user-friendly environment.

## Features

- **Interactive Browsing**: Easily navigate through cities, universities, faculties, and departments using intuitive dropdown menus.
- **Detailed Information Display**: View detailed information about each academic unit, including lists of departments and subjects.
- **Quick Search**: Search for universities, faculties, or departments by name.
- **System Statistics**: Access a dedicated section providing overall statistics about the number of universities, faculties, departments, and subjects, as well as breakdowns by city.
- **Data Export**: Export the entire university dataset to a JSON file for external use or analysis.
- **User-Friendly Interface**: Built with Tkinter, featuring a clean, modern design with clear navigation and information presentation.

## Installation

To run this application, you need Python 3.x installed on your system. No additional libraries are required beyond the standard Tkinter library, which is usually included with Python installations.

1. **Clone the repository (or download the files):**
   ```bash
   git clone https://github.com/your-username/kosovo-universities-gui.git
   cd kosovo-universities-gui
   ```

2. **Ensure Python 3 is installed:**
   ```bash
   python3 --version
   ```
   If Python 3 is not installed, please download it from [python.org](https://www.python.org/downloads/).

## Usage

To start the application, navigate to the project directory in your terminal and run the main script:

```bash
python3 kosovo_universities_gui.py
```

### Navigating the GUI

1.  **Select City**: Use the "Select City" dropdown to filter universities by location. Choose "All Cities" to view all universities.
2.  **Select University**: After selecting a city (or all cities), choose a university from the "Select University" dropdown.
3.  **Select Faculty**: Once a university is selected, pick a faculty from the "Select Faculty" dropdown to see its departments and subjects.
4.  **Quick Search**: Type in the "Quick Search" box to find specific universities, faculties, or departments.
5.  **Information Display**: The right panel will dynamically update to show information based on your selections or search queries.
6.  **Tabs**: Use the "Main Information" and "Detailed View" tabs to switch between different levels of detail.
7.  **Clear All**: Click the "Clear All" button to reset all selections and return to the welcome screen.
8.  **Show Statistics**: Click the "Show Statistics" button to open a new window displaying various system statistics.
9.  **Export Data**: Use `File > Export Data` from the menu bar to save the entire dataset as a JSON file.

## Data Structure

The application uses a hierarchical data structure to organize information:

-   **Cities (`QYTETET`)**: A dictionary mapping numerical IDs to city names in Kosovo.
-   **University**: Represents a university with attributes like `name`, `city`, and a list of `Faculty` objects.
-   **Faculty**: Represents a faculty with its `name` and a list of `Department` objects.
-   **Department**: Represents a specific academic program with its `name` and a list of `subjects`.

This structure allows for easy navigation and detailed representation of the academic landscape.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please feel free to:

1.  Fork the repository.
2.  Create a new branch (`git checkout -b feature/YourFeature`).
3.  Make your changes.
4.  Commit your changes (`git commit -m 'Add some feature'`).
5.  Push to the branch (`git push origin feature/YourFeature`).
6.  Open a Pull Request.

## License

This project is open-source and available under the MIT License.

## Contact

Email: dawa.sadiku@outlook.com

For any questions or feedback, please open an issue on the GitHub repository.