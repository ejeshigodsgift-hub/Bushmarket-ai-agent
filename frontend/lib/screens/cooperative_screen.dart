import 'package:flutter/material.dart';

class CooperativeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Cooperatives")),

      body: ListView(
        padding: EdgeInsets.all(16),

        children: [
          Text(
            "Active Cooperatives",
            style: TextStyle(
              fontSize: 18,
              fontWeight: FontWeight.bold,
            ),
          ),

          SizedBox(height: 20),

          ElevatedButton(
            onPressed: () {
              // call CoopService.createCoop()
            },
            child: Text("Create Cooperative"),
          ),
        ],
      ),
    );
  }
}