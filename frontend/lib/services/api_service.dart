import 'dart:convert';
import 'package:http/http.dart' as http;

class ApiService {
  static const String baseUrl =
      "https://your-railway-app.up.railway.app";

  // ========================
  // GET MARKETS
  // ========================
  static Future getMarkets() async {
    final res = await http.get(
      Uri.parse("$baseUrl/market/gallery"),
    );

    if (res.statusCode != 200) {
      throw Exception("Failed to load markets");
    }

    return jsonDecode(res.body);
  }

  // ========================
  // LOGIN
  // ========================
  static Future login(String username, String password) async {
    final res = await http.post(
      Uri.parse("$baseUrl/auth/login"),
      body: jsonEncode({
        "username": username,
        "password": password,
      }),
      headers: {
        "Content-Type": "application/json",
      },
    );

    if (res.statusCode != 200) {
      throw Exception("Login failed");
    }

    return jsonDecode(res.body);
  }

  // ========================
  // GET WALLET
  // ========================
  static Future getWallet(String token) async {
    final res = await http.get(
      Uri.parse("$baseUrl/wallet/balance"),
      headers: {
        "Authorization": "Bearer $token",
      },
    );

    if (res.statusCode != 200) {
      throw Exception("Failed to fetch wallet");
    }

    return jsonDecode(res.body);
  }

  // ========================
  // GET PRODUCTS
  // ========================
  static Future getProducts(String category) async {
    final res = await http.get(
      Uri.parse("$baseUrl/market/$category"),
    );

    if (res.statusCode != 200) {
      throw Exception("Failed to load products");
    }

    return jsonDecode(res.body);
  }

  // ========================
  // CHECKOUT
  // ========================
  static Future checkout(
      Map<String, dynamic> data, String token) async {
    final res = await http.post(
      Uri.parse("$baseUrl/market/checkout"),
      body: jsonEncode(data),
      headers: {
        "Content-Type": "application/json",
        "Authorization": "Bearer $token",
      },
    );

    if (res.statusCode != 200) {
      throw Exception("Checkout failed");
    }

    return jsonDecode(res.body);
  }
}