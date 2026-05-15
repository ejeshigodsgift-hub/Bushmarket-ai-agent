import 'package:flutter/material.dart';

class AIChatScreen extends StatefulWidget {
  @override
  State<AIChatScreen> createState() => _AIChatScreenState();
}

class _AIChatScreenState extends State<AIChatScreen> {
  List<String> messages = [];
  TextEditingController controller = TextEditingController();

  void sendMessage(String msg) {
    setState(() {
      messages.add("You: $msg");
    });

    controller.clear();

    // TODO: send to backend AI later
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Bushmarket AI")),
      body: Column(
        children: [
          Expanded(
            child: ListView.builder(
              itemCount: messages.length,
              itemBuilder: (context, index) {
                return ListTile(
                  title: Text(messages[index]),
                );
              },
            ),
          ),

          Padding(
            padding: EdgeInsets.all(10),
            child: TextField(
              controller: controller,
              onSubmitted: sendMessage,
              decoration: InputDecoration(
                hintText: "Ask Bushmarket AI...",
                border: OutlineInputBorder(),
              ),
            ),
          )
        ],
      ),
    );
  }
}