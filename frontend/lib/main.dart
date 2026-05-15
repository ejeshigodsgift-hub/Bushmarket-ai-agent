import 'package:flutter/material.dart';
import 'routes/app_routes.dart';
import 'theme/app_theme.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(BushmarketApp());
}

class BushmarketApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Bushmarket",

      debugShowCheckedModeBanner: false,

      theme: AppTheme.theme,

      initialRoute: "/home",

      routes: AppRoutes.routes,
    );
  }
}