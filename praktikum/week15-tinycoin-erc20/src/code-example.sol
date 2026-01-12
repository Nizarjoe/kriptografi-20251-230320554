// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

/*
 * TinyCoin ERC20
 * Nama  : Muhammad Nizar Asagaf
 * NIM   : 230320554
 * Kelas : 5 DSRA
 *
 * Kontrak ini menggunakan OpenZeppelin ERC20
 * untuk menjamin keamanan dan kepatuhan standar.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {

    /*
     * Constructor akan dijalankan sekali saat deployment
     * initialSupply ditentukan dalam satuan token terkecil (wei-like)
     * contoh: 1.000.000 token = 1000000 * 10**18
     */
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        _mint(msg.sender, initialSupply);
    }

}
