# End-to-End Web3 dApps: certificate generation, distribution, and value transfer with Algorand NFTs and smart contracts

## Business Objective
An organization (10 Academy), aware of the user controlled internet technology (Web3), would like to use it to deliver certificates to its trainees. The challenge is to ensure that certificates are available to all trainees in a secure way, and (if possible) that certificate holders can benefit from smart contract actions now and in the future. To solve this challenge, the Algorand Blockchain will be used to generate and distribute Non-Fungible Tokens (NFTs) as certificates to 10 Academy trainees. To do that, we will build an end-to-end Web3 dapps on the Algorand Blockchain that will help 10 Academy generate trainees’s certificates that will represent the successful completion of a weekly challenge to trainees, and allow trainees with NFTs to interact with a smart contract to perform predefined actions. Before going to the dapp for certificate generation, it’s important to have a look at Web3 technology and its related concepts.

## Web3 technology
Web3 is a recent technology developed to improve, solve and overcome the limitations of its predecessor (Web2). Despite the improvement provided by web2 through the development of cookies and centralized services, it was not able to solve these two problems:
Hold “state” independent of trusted operators: only the service providers have control over their state provided and the user does not have any control over which provider is giving them state or have access to their state.
Transfer state: there is no way for the user to transfer his state.
Thus, Web3 known as a user controlled internet comes into play with its amazing advance providing these solutions:
The creation of native economic value by any participant; and
The transfer of this native value to any participant.
WIth Web3 a user can hold his state and transfer it: this can be seen as the main difference between Web2 and Web3.
Web3 technology has been developed starting from blockchains (concepts explained later on in this document) that provide a way to hold state. The web3 stack currently looks like in the below figure. It is made up of modular components that allow state to be shared among all participants while preventing vendor lock-in to layers below. Because of this, if an application wants to change the state layer, it does not need to rewrite its entire stack (i.e. blockchain). This is effective because it fosters healthy competition and allows each layer to preserve the value it creates without having to worry about what will happen if the rules of the game change later on.

![web3_stack](https://user-images.githubusercontent.com/110104014/192861441-5ed79837-0528-4da9-ba1f-929d05f2244e.png)

Let’s have a look at two important layers of the above stack: the state layer and the user control layer.
 - The State Layer: The state layer preserves the state of all that happens below it. It is almost exclusively provided by blockchain infrastructure and allows for any participant to take part as long as they obey the rules of the preferred network. This layer can either be a public or private/permissioned layer. 
 - The User Control Layer: the main functionality of this layer is to manage a user’s private keys and be able to sign transactions on the State Layer. A transaction at the State Layer changes the state of a user’s account and hence is at the core of how users interact with Web 3 applications. This lies in the use of wallets.

### Web3 applications architecture
Let’s compare the architecture of Web2 and Web3 applications (following figure). **The dapp built in this project will have a similar architecture

![web3_app_architecture](https://user-images.githubusercontent.com/110104014/192861882-d7c36250-a693-416a-81ed-013321732c4d.png)

A simplistic version of today’s Web 2.0 architecture includes a client software, usually a browser or a self-contained application, and a suite of servers providing content and logic, which are all controlled by the same entity. Web 3.0 architecture leverages what’s enabled by a universal State Layer. It does this by allowing two things:

 1. Allowing applications to place some or all of their content and logic on to a public blockchain. Contrary to standard Web 2.0, this content and logic can become public and accessible by anyone.
 2. Allowing users to exert direct control over this content and logic. Unlike Web 2.0, users don’t necessarily need accounts or privileged API keys to interact with what’s on the blockchain.

The main key used by Web3 to enable this is the wallet. Modern wallets, such as Coinbase Wallet, interact with the main client front-end to provide a seamless user experience, in addition to serving as the User Control Layer for the Web 3 stack. They accomplish this by allowing applications to send requests to the wallet itself via standard libraries, the most popular of which is web3.js. A payment request, for example, could be a web3.js call that asks the user to confirm that the wallet can send a specified amount of funds to the application's address. When a user accepts, two things occur: 1) The wallet responds to the application front-end, allowing it to display a "Payment Submitted" screen; 2) the wallet makes an RPC call to the blockchain server, submitting the approved transaction to the blockchain.

### What is Blockchain and how does it work?
A blockchain is a shared database on a network of computers. Once a record has been added to the chain, it is very difficult to change it. To ensure that all copies of the database are identical, the network performs constant checks. Blockchains have been used to support cyber currencies like bitcoin, but many other possible uses are emerging. [This link](http://graphics.reuters.com/TECHNOLOGY-BLOCKCHAIN/010070P11GN/index.html) provides full details on how blockchains work.

## Application in the current project
This project will build a [decentralized application](https://developer.algorand.org/docs/get-started/dapps/) based on the technology described above. It will integrate the use of the wallet that will help to sign in a secure way a transaction. The certificates will be generated as assets. The assets will be non-fungible to make them unique: there will be NFTs. Let’s have a look at what an asset is in Algorand Blockchain.

Look at the readme file in respectively frontend and backend folder for information about frontend and backend development.

### Account and Assets in Algorand Block
The Algorand protocol enables the creation of on-chain assets that share the Algo's security, compatibility, speed, and ease of use. Algorand Standard Assets (ASA) is the official name for assets on Algorand.
Algorand Standard Assets can be used to represent stablecoins, loyalty points, system credits, and in-game points, to name a few. One can also represent single, unique assets such as a house deed, collectible items, unique parts of a supply chain, and so on. There is also the option to place transfer restrictions on an asset, which can help with securities, compliance, and certification use cases.

## Important references
https://developer.algorand.org/docs/get-started/dapps/  
https://www.coinbase.com/blog/understanding-web-3-a-user-controlled-internet  
http://graphics.reuters.com/TECHNOLOGY-BLOCKCHAIN/010070P11GN/index.html  

