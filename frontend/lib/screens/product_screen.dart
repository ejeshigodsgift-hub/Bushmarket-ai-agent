import 'package:flutter/material.dart';

class ProductScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Products")),
      body: Column(
        children: [
          Text("Product List"),
          Text("Gate Pass will be added at checkout"),
          ElevatedButton(
            onPressed: () {},
            child: Text("Add to Cart"),
          )
        ],
      ),
    );
  }
}