import 'package:shared_preferences/shared_preferences.dart';

class LocalStorage {
  // SAVE TOKEN
  static Future<void> saveToken(String token) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString("token", token);
  }

  // GET TOKEN
  static Future<String?> getToken() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getString("token");
  }

  // REMOVE TOKEN (LOGOUT)
  static Future<void> removeToken() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove("token");
  }
}