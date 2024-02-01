# SUMS News Categories

This code will get all news articles and their associated categories. This interacts with Sums' [Pluto API](https://github.com/University-of-Lincoln-SU/External-Developer-Docs/tree/master/PlutoAPI).

## Installation

Follow these steps to install and run the script:

1. **Clone the repository**

    First, clone the repository to your local machine using git. Open your terminal and run:

    ```bash
    git clone https://github.com/YUSU-Dev/sums-news-categories
    ```

2. **Navigate to the project directory**

    Change your current directory to the project directory:

    ```bash
    cd <project_directory>
    ```

    Replace `<project_directory>` with the name of the directory that was created when you cloned the repository.

3. **Create a virtual environment (optional)**

    It's recommended to create a virtual environment to isolate the Python and pip packages used by this project. Use the following command to create a new virtual environment:

    ```bash
    python3 -m venv env
    ```

    Then, activate the virtual environment:

    - On macOS and Linux:

        ```bash
        source env/bin/activate
        ```

    - On Windows:

        ```bash
        .\env\Scripts\activate
        ```

4. **Install the required packages**

    Install the required Python packages using pip:

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the script**

    Finally, you can run the script using the following command:

    ```bash
    python main.py
    ```

    The script will prompt you to enter your X-Site-Id. After you enter it, the script will fetch the data and write it into a CSV file named 'data.csv'.
