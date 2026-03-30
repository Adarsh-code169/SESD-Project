export interface Product {
  _id: string;
  name: string;
  price: number;
  offerPrice: number;
  description: string[];
  image: string[];
  category: string;
  inStock: boolean;
  weight?: string;
}

export interface User {
  _id: string;
  name: string;
  email: string;
  cartItems: Record<string, number>;
}

export interface Address {
  _id: string;
  userId: string;
  firstName: string;
  lastName: string;
  email: string;
  street: string;
  city: string;
  state: string;
  zipcode: number;
  country: string;
  phone: string;
}

export interface OrderItem {
  productId: string | Product | any;
  quantity: number;
}

export interface Order {
  _id: string;
  userId: string;
  items: OrderItem[];
  amount: number;
  address: string | Address | any;
  status: string;
  paymentType: string;
  isPaid: boolean;
  createdAt: string;
}

export interface AppContextType {
  navigate: any;
  user: User | null;
  setUser: (user: User | null) => void;
  isSeller: boolean;
  setIsSeller: (isSeller: boolean) => void;
  showUserLogin: boolean;
  setShowUserLogin: (show: boolean) => void;
  showSellerLogin: boolean;
  setShowSellerLogin: (show: boolean) => void;
  products: Product[];
  currency: string;
  addToCart: (itemId: string) => void;
  updateCartItem: (itemId: string, quantity: number) => void;
  removeFromCart: (itemId: string) => void;
  cartItems: Record<string, number>;
  searchQuery: string;
  setSearchQuery: (query: string) => void;
  getCartCount: () => number;
  getCartAmount: () => number;
  axios: any;
  fetchProducts: () => Promise<void>;
  setCartItems: (items: Record<string, number>) => void;
}
