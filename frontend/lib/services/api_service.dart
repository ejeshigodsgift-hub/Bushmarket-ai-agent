import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const baseUrl = "https://your-railway-app.up.railway.app";

  static Future getMarkets() async {
    final res = await http.get(Uri.parse("$baseUrl/market/gallery"));
    return jsonDecode(res.body);
  }

  static Future login(data) async {
    final res = await http.post(
      Uri.parse("$baseUrl/auth/login"),
      body: jsonEncode(data),
      headers: {"Content-Type": "application/json"},
    );
    return jsonDecode(res.body);
  }

  static Future getWallet(token) async {
    final res = await http.get(
      Uri.parse("$baseUrl/wallet/balance"),
      headers: {"Authorization": "Bearer $token"},
    );
    return jsonDecode(res.body);
  }
}


static Future login(String username, String password) async {
  final res = await http.post(
    Uri.parse("$baseUrl/auth/login"),
    body: jsonEncode({
      "username": username,
      "password": password
    }),
    headers: {"Content-Type": "application/json"},
  );

  return jsonDecode(res.body);
}