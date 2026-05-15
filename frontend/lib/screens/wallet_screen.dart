import 'package:flutter/material.dart';

class WalletScreen extends StatelessWidget {

  void deposit() {
    // TODO: connect payment gateway later
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Wallet")),

      body: Padding(
        padding: EdgeInsets.all(16),

        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,

          children: [

            Text(
              "Balance: ₦0",
              style: TextStyle(
                fontSize: 22,
                fontWeight: FontWeight.bold,
              ),
            ),

            SizedBox(height: 20),

            ElevatedButton(
              onPressed: deposit,
              child: Text("Deposit"),
            ),
          ],
        ),
      ),
    );
  }
}