import 'package:flutter/material.dart';

class WalletScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Wallet")),
      body: Column(
        children: [
          Text("Balance: ₦0"),
          ElevatedButton(
            onPressed: () {},
            child: Text("Deposit"),
          )
        ],
      ),
    );
  }
}