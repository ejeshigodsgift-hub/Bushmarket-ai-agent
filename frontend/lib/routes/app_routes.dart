import 'package:flutter/material.dart';

import '../screens/home_screen.dart';
import '../screens/market_gallery_screen.dart';
import '../screens/cooperative_screen.dart';
import '../screens/wallet_screen.dart';
import '../screens/ai_chat_screen.dart';

class AppRoutes {
  static Map<String, WidgetBuilder> routes = {
    "/home": (context) => HomeScreen(),
    "/market": (context) => MarketGalleryScreen(),
    "/coop": (context) => CooperativeScreen(),
    "/wallet": (context) => WalletScreen(),
    "/ai": (context) => AIChatScreen(),
  };
}