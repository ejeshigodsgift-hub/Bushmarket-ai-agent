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


static Future createCoop(data, token) async {
  final res = await http.post(
    Uri.parse("$baseUrl/cooperative/create"),
    body: jsonEncode(data),
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer $token"
    },
  );

  return jsonDecode(res.body);
}