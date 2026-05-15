import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Bushmarket")),
      body: Column(
        children: [
          Text("AI Assistant"),
          ElevatedButton(
            onPressed: () {
              Navigator.pushNamed(context, "/ai-chat");
            },
            child: Text("Chat with AI"),
          ),
          ElevatedButton(
            onPressed: () {
              Navigator.pushNamed(context, "/market");
            },
            child: Text("Commodity Gallery"),
          ),
        ],
      ),
    );
  }
}


Scaffold(
  appBar: AppBar(title: Text("Bushmarket")),
  body: GridView.count(
    crossAxisCount: 2,
    children: [
      menu("Markets", "/market"),
      menu("Cooperatives", "/coop"),
      menu("Wallet", "/wallet"),
      menu("AI Chat", "/ai"),
    ],
  ),
);