# MT5 WRAPPER
MT5 Wrapper is a Python package that wraps around the MetaTrader5 library, adding type annotations and improving the developer experience with better IntelliSense, autocomplete, and code readability.

### Features
 - **Type Annotations**: Provides clear type hints for all major mt5 functions and classes.
 - **Improved IntelliSense**: Get accurate autocomplete suggestions in your favorite IDEs like VS Code or PyCharm.
 - **Enhanced Readability**: Makes working with the mt5 library easier and more error-free.

### Installation
`pip install mt5-wrapper`


### Getting Started
Here's a quick example of using mt5_wrapper:
```
import mt5_wrapper as mt5
mt5.initialize()

# get some account info
account_info = mt5.account_info()

if account_info: # not adding this check will display an errpr in IDE
    print(account_info.name)

mt5.shutdown()
```

### Requirements
 - Python 3.10 or later
 - MetaTrader5 terminal installed
 - MetaTrader5 Python package (installed automatically as a dependency)

### Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request to improve the package.

### License
This project is licensed under the MIT License.













