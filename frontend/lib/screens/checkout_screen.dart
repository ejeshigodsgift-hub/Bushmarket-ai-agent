import 'package:flutter/material.dart';

class CheckoutScreen extends StatelessWidget {
  final double total;
  final double delivery;
  final double gatePass;

  CheckoutScreen({
    required this.total,
    required this.delivery,
    required this.gatePass,
  });

  double get finalTotal => total + delivery + gatePass;

  void checkout() {
    // TODO: connect to backend payment API
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Checkout")),
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text("Product Total: ₦$total"),
            Text("Delivery Fee: ₦$delivery"),
            Text("Gate Pass Fee: ₦$gatePass"),
            SizedBox(height: 10),
            Text(
              "Final Total: ₦$finalTotal",
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: checkout,
              child: Text("Pay Now"),
            )
          ],
        ),
      ),
    );
  }
}