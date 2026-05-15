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


ListView.builder(
  itemCount: products.length,
  itemBuilder: (context, index) {
    return Card(
      child: Column(
        children: [
          Image.network(products[index]["image"]),
          Text(products[index]["name"]),
          Text("₦${products[index]["price"]}"),
          Text(products[index]["unit"]),
        ],
      ),
    );
  },
);