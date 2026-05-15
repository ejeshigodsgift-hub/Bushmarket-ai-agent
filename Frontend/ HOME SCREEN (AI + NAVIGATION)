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