import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(BushmarketApp());
}

class BushmarketApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: "Bushmarket",
      home: HomeScreen(),
    );
  }
}