# AtomicTrades: Decentralized NFT Marketplace Scaffold

A robust and gas-optimized foundation for building decentralized NFT marketplaces, featuring on-chain royalties, curated listings, and secure off-chain approvals using EIP-712 signatures.

## Detailed Description

AtomicTrades provides a sophisticated scaffold for creating decentralized NFT marketplaces, addressing key challenges around security, efficiency, and creator rights. The project is built upon the principle of on-chain royalty enforcement, ensuring that creators receive their due compensation with every secondary sale. This is achieved through smart contract logic that automatically distributes a percentage of the sale price to the original artist, transparently and immutably.

The platform leverages curated listings to enhance the user experience and combat the proliferation of spam or unauthorized content. This feature allows marketplace operators to define criteria for NFT listings, ensuring that only approved assets are presented to users. A governance mechanism (e.g., DAO or multisig) can be implemented to manage these listings, creating a more trustworthy and valuable marketplace environment.

A critical component of AtomicTrades is its utilization of EIP-712 signatures for off-chain approvals. Instead of requiring users to approve each transaction individually on-chain (which can be costly in terms of gas), the platform allows users to sign messages off-chain that authorize specific trades. These signed messages are then submitted to the smart contract, significantly reducing gas fees associated with trade approvals. This approach also enhances user experience by streamlining the trading process. The implementation is carefully crafted to prevent replay attacks and ensure the integrity of the signed messages.

AtomicTrades aims to empower developers with a production-ready foundation to build their own NFT marketplaces, customized to their specific needs. This scaffold provides the core functionalities required for a successful marketplace, while allowing for extensibility and customization through modular smart contract design. By focusing on gas optimization, creator royalties, and curated listings, AtomicTrades strives to improve the NFT ecosystem and offer a superior trading experience.

## Key Features

*   **On-Chain Royalties:** Royalty payments are enforced directly within the smart contract, ensuring creators automatically receive a percentage of each sale price. The royalty percentage is configurable per NFT collection.
*   **Curated Listings:** A listing management system allows for the controlled addition of NFTs to the marketplace, preventing spam and ensuring quality.
*   **EIP-712 Signature Approvals:** Users can authorize trades off-chain using EIP-712 signatures, significantly reducing gas costs associated with approvals. This leverages eth_signTypedData_v4.
*   **Gas-Optimized Smart Contracts:** The smart contracts are designed with gas efficiency in mind, minimizing transaction costs for users. Careful selection of data types and storage patterns contributes to lower gas consumption.
*   **Modular Design:** The smart contracts are designed in a modular fashion, making it easy to extend and customize the platform with new features.
*   **Secure Implementation:** Stringent security audits and testing are performed to ensure the security and integrity of the smart contracts.
*   **Upgradeable Contracts (Optional):** The contracts can be deployed as upgradeable proxy contracts using the UUPS or Transparent Proxy pattern to ensure future extensibility and bug fixes.

## Technology Stack

*   **Python:** Used for development scripts, testing, and potentially off-chain components.
*   **Solidity:** The primary language for writing smart contracts, responsible for the marketplace logic, royalty enforcement, and EIP-712 signature verification.
*   **Hardhat:** A development environment for compiling, deploying, testing, and interacting with Solidity smart contracts.
*   **Ethers.js/Web3.py:** JavaScript/Python libraries used for interacting with the Ethereum blockchain and smart contracts from client-side applications or backend services.
*   **OpenZeppelin Contracts:** A library of secure and reusable smart contract components, used for implementing EIP-721 and other standards.

## Installation

1.  **Prerequisites:**
    *   Node.js (v16 or higher)
    *   Python 3.8 or higher
    *   npm or yarn
    *   Ganache CLI (optional, for local development)

2.  **Clone the repository:**
    git clone https://github.com/ezozu/AtomicTrades.git
    cd AtomicTrades

3.  **Install dependencies:**
    npm install

    or

    yarn install

4.  **Install Python dependencies (optional, for running Python scripts):**
    pip install -r requirements.txt

## Configuration

1.  **Environment Variables:**
    Create a `.env` file in the root directory with the following environment variables:

    PRIVATE_KEY=your_private_key
    RPC_URL=your_rpc_url (e.g., Infura or Alchemy endpoint)
    CHAIN_ID=your_chain_id (e.g., 1 for Ethereum Mainnet, 5 for Goerli)

2.  **Hardhat Configuration:**
    The `hardhat.config.js` file contains network configurations. Update the `networks` section with your RPC URL and private key.

3.  **Smart Contract Addresses:**
    After deploying the smart contracts, update the addresses in the frontend or backend configuration files to point to the deployed contract instances.

## Usage

1.  **Compile Smart Contracts:**
    npx hardhat compile

2.  **Deploy Smart Contracts:**
    npx hardhat deploy --network <network_name>

    For example:

    npx hardhat deploy --network goerli

3.  **Run Tests:**
    npx hardhat test

4.  **Interact with Smart Contracts:**

    Using Ethers.js (example):

    import { ethers } from "ethers";
    const marketplaceAddress = "0x..."; // Deployed marketplace contract address
    const marketplaceABI = [...]; // Marketplace contract ABI

    async function buyNFT(tokenId) {
        const provider = new ethers.providers.JsonRpcProvider(process.env.RPC_URL);
        const signer = new ethers.Wallet(process.env.PRIVATE_KEY, provider);
        const marketplaceContract = new ethers.Contract(marketplaceAddress, marketplaceABI, signer);

        const price = await marketplaceContract.getListingPrice(tokenId);
        const transaction = await marketplaceContract.buyNFT(tokenId, { value: price });
        await transaction.wait();
        console.log("NFT bought successfully!");
    }

5. **Generating EIP-712 Signatures:**
    A python script `scripts/generate_signature.py` can be used for generating off-chain signatures. It requires the user's address, contract address, nonce, and other relevant parameters.

## Contributing

We welcome contributions to AtomicTrades! Please follow these guidelines:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Write clear and concise commit messages.
4.  Submit a pull request with a detailed description of your changes.
5.  Ensure your code adheres to the project's coding standards.
6.  Include tests for your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ezozu/AtomicTrades/blob/main/LICENSE) file for details.

## Acknowledgements

We would like to thank the open-source community for their contributions to the Ethereum ecosystem, particularly the developers of Hardhat, Ethers.js, and OpenZeppelin Contracts.