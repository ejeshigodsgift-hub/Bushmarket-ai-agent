Text("Product Total: ₦1000"),
Text("Delivery Fee: ₦200"),
Text("Gate Pass Fee: ₦500"),
Text("Final Total: ₦1700"),


Column(
  children: [
    Text("Product Total: ₦${total}"),
    Text("Delivery: ₦${delivery}"),
    Text("Gate Pass: ₦${gatePass}"),
    Text("Final: ₦${total + delivery + gatePass}"),
    ElevatedButton(
      onPressed: () => checkout(),
      child: Text("Pay Now"),
    )
  ],
);