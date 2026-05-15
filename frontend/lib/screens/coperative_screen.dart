import 'package:flutter/material.dart';

class CooperativeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Cooperatives")),
      body: Column(
        children: [
          Text("Join or Create Cooperative"),
          ElevatedButton(
            onPressed: () {},
            child: Text("Create Cooperative"),
          )
        ],
      ),
    );
  }
}