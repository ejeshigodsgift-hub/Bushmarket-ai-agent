import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  Widget menu(BuildContext context, String title, String route) {
    return GestureDetector(
      onTap: () => Navigator.pushNamed(context, route),
      child: Card(
        child: Center(child: Text(title)),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Bushmarket")),
      body: GridView.count(
        crossAxisCount: 2,
        children: [
          menu(context, "Markets", "/market"),
          menu(context, "Cooperatives", "/coop"),
          menu(context, "Wallet", "/wallet"),
          menu(context, "AI Chat", "/ai"),
        ],
      ),
    );
  }
}