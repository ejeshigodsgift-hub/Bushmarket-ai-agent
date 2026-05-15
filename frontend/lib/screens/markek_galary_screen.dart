import 'package:flutter/material.dart';

class MarketScreen extends StatelessWidget {
  final markets = [
    "Rice Market",
    "Palm Oil Market",
    "Fish Market",
    "Beans Market"
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Commodity Gallery")),
      body: ListView.builder(
        itemCount: markets.length,
        itemBuilder: (context, index) {
          return ListTile(
            title: Text(markets[index]),
            onTap: () {
              Navigator.pushNamed(context, "/products");
            },
          );
        },
      ),
    );
  }
}


FutureBuilder(
  future: ApiService.getProducts("Rice"),
  builder: (context, snapshot) {
    return ListView(
      children: snapshot.data.map((p) => productCard(p)).toList(),
    );
  },
);