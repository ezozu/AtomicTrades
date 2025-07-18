# AtomicTrades: A Minimalist Trading Framework

AtomicTrades provides a lightweight and flexible framework for building automated trading systems. Designed with simplicity and extensibility in mind, AtomicTrades allows developers to quickly prototype and deploy trading strategies across various financial markets. The core principle is to provide a robust foundation while minimizing dependencies, empowering users to customize and optimize the system according to their specific needs.

The primary purpose of AtomicTrades is to abstract away the complexities of interacting with market data feeds and order execution platforms, offering a clean and intuitive API. It handles tasks such as data normalization, connection management, and error handling, freeing developers to focus on strategy logic and risk management. The framework emphasizes modularity, enabling easy integration of custom components, including data connectors, indicator libraries, and order routing algorithms. This makes AtomicTrades suitable for both individual traders and small teams looking to develop and test their trading ideas without the overhead of complex and bloated trading platforms.

AtomicTrades stands out by offering a minimalist approach. Unlike comprehensive trading platforms with a myriad of built-in features, AtomicTrades focuses on providing a core set of functionalities essential for automated trading. This reduces the learning curve and allows users to quickly grasp the underlying architecture. The modular design enables incremental development and customization, ensuring that the system remains lean and efficient. Furthermore, the framework promotes a "bring your own" philosophy, allowing users to leverage their preferred data sources, charting libraries, and analytical tools.

## Key Features

*   **Real-time Data Ingestion:** Supports integration with various market data providers through a flexible data connector interface. Specific implementations (e.g., connecting to a REST API or a Websocket stream) require extending the `AbstractDataConnector` class. The framework handles data normalization and time series management internally.

*   **Order Execution Management:** Provides an abstract order execution interface, enabling integration with different brokers and exchanges. The framework supports market orders, limit orders, and stop orders. Specific broker integrations require implementing the `AbstractOrderExecutor` class.

*   **Strategy Backtesting:** Includes a backtesting engine that allows users to test their trading strategies on historical data. The engine supports various performance metrics, including profit factor, drawdown, and Sharpe ratio. Backtesting uses the same data connector interface as live trading, ensuring consistency between backtesting and live environments.

*   **Risk Management:** Offers a flexible risk management framework that allows users to define custom risk parameters, such as position limits, stop-loss orders, and maximum drawdown thresholds. The risk management module integrates seamlessly with the order execution module to prevent excessive risk-taking.

*   **Event-Driven Architecture:** Built on an event-driven architecture, allowing for real-time response to market events. The framework uses a message queue to decouple components and improve scalability. Custom event handlers can be easily registered to respond to specific market events.

*   **Modular Design:** The framework is designed with modularity in mind, enabling easy integration of custom components. Users can extend the framework by creating their own data connectors, order executors, indicators, and risk management modules.

## Technology Stack

*   **Python 3.x:** The core programming language for the framework, chosen for its readability, extensive libraries, and rapid prototyping capabilities.
*   **Pandas:** Used for data manipulation and analysis, providing efficient data structures for time series management and backtesting.
*   **NumPy:** Provides support for numerical computations, including statistical analysis and technical indicator calculations.
*   **Requests/Websockets:** Used for interacting with market data APIs and order execution platforms. The specific library depends on the requirements of the data connector or order executor.
*   **Threading/Asyncio:** Used for concurrent execution of tasks, enabling efficient data ingestion and order execution.

## Installation

1.  **Clone the repository:**

    git clone https://github.com/ezozu/AtomicTrades.git
    cd AtomicTrades

2.  **Create a virtual environment:**

    python3 -m venv venv
    source venv/bin/activate (Linux/macOS)
    venv\Scripts\activate (Windows)

3.  **Install dependencies:**

    pip install -r requirements.txt

## Configuration

AtomicTrades relies on environment variables for sensitive information such as API keys and broker credentials. Create a `.env` file in the root directory of the project and populate it with the following variables (example):

DATA_PROVIDER_API_KEY=YOUR_DATA_PROVIDER_API_KEY
BROKER_API_KEY=YOUR_BROKER_API_KEY
BROKER_API_SECRET=YOUR_BROKER_API_SECRET
TRADING_SYMBOL=BTCUSDT

These variables can then be accessed within your code using the `os.environ` module. The `Config` class (defined in `config.py`) provides a convenient way to load and manage configuration settings.

## Usage

Example of connecting to a hypothetical data stream and printing the price:

from atomictrades.data import AbstractDataConnector
import time

class MyDataConnector(AbstractDataConnector):
    def __init__(self, api_key):
        super().__init__()
        self.api_key = api_key

    def connect(self):
        print("Connecting to data stream...")
        # Simulate connection setup
        time.sleep(1)
        print("Connected!")

    def get_price(self):
        # Simulate fetching price data
        time.sleep(0.1)
        return 42000.0

connector = MyDataConnector("YOUR_API_KEY")
connector.connect()

for i in range(5):
    price = connector.get_price()
    print(f"Price: {price}")
    time.sleep(1)

This showcases how to create a simple data connector. To integrate with actual market data and brokers, you will need to implement the `connect()` and `get_price()` methods (and related methods for submitting orders) using the appropriate API libraries. Refer to the example data connectors and order executors for more detailed examples.

## Contributing

We welcome contributions to AtomicTrades! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise code with proper documentation.
4.  Submit a pull request with a detailed description of your changes.
5.  Ensure that your code passes all unit tests.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ezozu/AtomicTrades/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for providing the libraries and tools that made this project possible.