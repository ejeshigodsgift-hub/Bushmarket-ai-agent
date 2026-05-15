import 'package:flutter/material.dart';

class AIChatScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Bushmarket AI")),
      body: Column(
        children: [
          Expanded(child: Container()),
          Padding(
            padding: EdgeInsets.all(10),
            child: TextField(
              decoration: InputDecoration(
                hintText: "Ask Bushmarket AI...",
              ),
            ),
          )
        ],
      ),
    );
  }
}



TextField(
  onSubmitted: (msg) {
    sendToBackend(msg);
  },
  decoration: InputDecoration(hintText: "Ask Bushmarket AI"),
)