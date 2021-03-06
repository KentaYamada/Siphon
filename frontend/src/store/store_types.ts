import { Authrication } from '@/entity/auth';
import { Sales } from '@/entity/sales';
import { Category } from '@/entity/category';
import { Item } from '@/entity/item';
import { User } from '@/entity/user';
import { DailySales } from '@/entity/daily_sales';
import { MonthlySales, PopularItem } from '@/entity/dashboard';

/** Auth state */
export interface AuthState {
    auth: Authrication;
    is_logged_in: boolean;
    auth_token: string;
    user_id?: number | null;
}

/** Cashier state */
export interface CashierState {
    sales: Sales;
    categories: Category[];
    items: Item[];
}

/** Category state */
export interface CategoryState {
    categories: Category[];
}

/** Daily sales state */
export interface DailySalesState {
    daily_sales: DailySales[];
}

/** Dashboard state */
export interface DashboardState {
    monthly_sales: MonthlySales[];
    popular_items: PopularItem[];
}

/** Item state */
export interface ItemState {
    items: Item[];
}

/** User state */
export interface UserState {
    users: User[];
}
