from django.urls import path

from .views import (
    create_store,
    only_store_list,
    StoreListView,
    StoreDetailView,
    update_store,
    delete_store,
)

app_name = "business"
urlpatterns = [
    path("create_store/", create_store, name="create_store"),
    path("update_store/<int:pk>", update_store, name="update_store"),
    path("delete_store/<int:pk>", delete_store, name="delete_store"),
    
    path("stores_list/", StoreListView.as_view(), name="stores_list"),
    path("store-detail/<int:pk>", StoreDetailView.as_view(), name="store_detail"),

    path("only_stores_list/", only_store_list, name="only_store_list"),

    # path("dashboard/inventory/load_subtable_hx/<int:item_id>", load_subtable_hx, name="load_subtable_hx"),

    # path("dashboard/inventory/alpine_toggle/<int:item_id>", alpine_toggle, name="alpine_toggle"),
    # path("dashboard/inventory/create_store/", create_store, name="create_store"),
    # path("dashboard/inventory/only_warehouse_list/", only_warehouse_list, name="only_warehouse_list"),
    # path("dashboard/inventory/load_items_view/", load_items_view, name="load_items_view"),
    # path("dashboard/inventory/export_warehouse_products", export_warehouse_products, name="export_warehouse_products"),
    # path("dashboard/inventory/export_warehouse_orders", export_warehouse_orders, name="export_warehouse_orders"),
    # path("dashboard/inventory/export_warehouse_transfers", export_warehouse_transfers, name="export_warehouse_transfers"),
]