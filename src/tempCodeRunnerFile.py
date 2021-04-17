ers = TrackOrders()
track_orders.add_new_order("jorge", "frango", "domingo")
track_orders.add_new_order("jorge", "frango", "domingo")
track_orders.add_new_order("arnaldo", "peixe", "sábado")
track_orders.add_new_order("maria", "carne", "sábado")
track_orders.add_new_order("joao", "salada", "segunda-feira")
less_busy = track_orders.get_least_busy_day()
assert "segunda-feira" == less_busy
