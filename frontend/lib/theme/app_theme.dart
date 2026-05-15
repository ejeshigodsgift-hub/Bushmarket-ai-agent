import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class AppTheme {

  // COLORS
  static const Color primaryGreen = Color(0xFF2E7D32);
  static const Color lightGreen = Color(0xFFA5D6A7);
  static const Color background = Color(0xFFF5F5F5);
  static const Color accentOrange = Color(0xFFFFA726);

  // THEME
  static ThemeData theme = ThemeData(

    primaryColor: primaryGreen,

    scaffoldBackgroundColor: background,

    textTheme: GoogleFonts.poppinsTextTheme(),

    appBarTheme: const AppBarTheme(
      backgroundColor: primaryGreen,
      foregroundColor: Colors.white,
    ),

    elevatedButtonTheme: ElevatedButtonThemeData(
      style: ElevatedButton.styleFrom(
        backgroundColor: primaryGreen,
        foregroundColor: Colors.white,
      ),
    ),
  );
}