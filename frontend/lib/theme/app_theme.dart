Color primaryGreen = Color(0xFF2E7D32);
Color lightGreen = Color(0xFFA5D6A7);
Color background = Color(0xFFF5F5F5);
Color accentOrange = Color(0xFFFFA726);

google_fonts: ^6.1.0


import 'package:flutter/material.dart';

class AppTheme {
  static ThemeData theme = ThemeData(
    primaryColor: Color(0xFF2E7D32),
    scaffoldBackgroundColor: Color(0xFFF5F5F5),

    appBarTheme: AppBarTheme(
      backgroundColor: Color(0xFF2E7D32),
      foregroundColor: Colors.white,
    ),

    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: Color(0xFF2E7D32),
        foregroundColor: Colors.white,
      ),
    ),
  );
}