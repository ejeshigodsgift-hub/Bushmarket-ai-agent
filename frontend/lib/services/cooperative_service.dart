import 'dart:convert';
import 'package:http/http.dart' as http;

class CoopService {
  static const baseUrl = "https://your-railway-app.up.railway.app";

  // CREATE COOPERATIVE
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

  // JOIN COOPERATIVE
  static Future joinCoop(int id, token) async {
    final res = await http.post(
      Uri.parse("$baseUrl/cooperative/join/$id"),
      headers: {
        "Authorization": "Bearer $token"
      },
    );

    return jsonDecode(res.body);
  }
}