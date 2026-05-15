import 'package:flutter/material.dart';
import '../services/api_service.dart';

class ProductScreen extends StatelessWidget {
  final String category;

  ProductScreen({required this.category});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(category)),

      body: FutureBuilder(
        future: ApiService.getProducts(category),

        builder: (context, snapshot) {

          if (!snapshot.hasData) {
            return Center(
              child: CircularProgressIndicator(),
            );
          }

          final products = snapshot.data;

          return ListView.builder(
            itemCount: products.length,

            itemBuilder: (context, index) {

              final p = products[index];

              return Card(
                child: Column(
                  children: [

                    Image.network(p["image"]),

                    Text(p["name"]),

                    Text("₦${p["price"]}"),

                    Text(p["unit"]),

                    Text(
                      "Gate Pass added during checkout",
                    ),

                    ElevatedButton(
                      onPressed: () {
                        // add to cart
                      },
                      child: Text("Add to Cart"),
                    )
                  ],
                ),
              );
            },
          );
        },
      ),
    );
  }
}