track_orders = TrackOrders()
track_orders.add_new_order("jorge", "frango", "domingo")
assert len(track_orders) == 1
