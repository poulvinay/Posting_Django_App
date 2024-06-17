# Posting_Django_App
This is Web Appilication developed with Python Django framework.
package newcc;
import java.util.LinkedList;
import java.util.Stack;
import java.util.Queue;

public class ShoppingApp {
    public static void main(String[] args) {
        // Creating instances of Shopping Cart, Purchase History, and Customer Service
        ShoppingCart cart = new ShoppingCart();
        PurchaseHistory history = new PurchaseHistory();
        CustomerService service = new CustomerService();

        // Adding items to the shopping cart
        cart.addItem("Laptop");
        cart.addItem("Mouse");
        cart.addItem("Keyboard");

        // Viewing items in the shopping cart
        cart.viewCart();

        // Removing an item from the shopping cart
        cart.removeItem("Mouse");

        // Viewing updated shopping cart
        cart.viewCart();

        // Saving current cart to purchase history
        LinkedList<String> currentCart = new LinkedList<>(cart.getCart()); // Create a copy of the cart
        history.addToHistory(currentCart);

        // Viewing purchase history
        history.viewHistory();

        // Undoing the last purchase
        LinkedList<String> lastCart = history.undoLastPurchase();
        System.out.println("Last purchase undone: " + lastCart);

        // Adding customer service requests
        service.addRequest("Issue with payment");
        service.addRequest("Product return request");

        // Viewing pending customer service requests
        service.viewRequests();

        // Processing customer service requests
        service.processRequest();
        service.processRequest();
        service.processRequest();
    }
}

// Shopping Cart class
class ShoppingCart {
    private LinkedList<String> cart;

    public ShoppingCart() {
        cart = new LinkedList<>();
    }

    public void addItem(String item) {
        cart.add(item);
    }

    public void removeItem(String item) {
        cart.remove(item);
    }

    public void viewCart() {
        if (cart.isEmpty()) {
            System.out.println("The cart is empty.");
        } else {
            System.out.println("Items in the cart:");
            for (String item : cart) {
                System.out.println(item);
            }
        }
    }

    public LinkedList<String> getCart() {
        return cart;
    }
}

// Purchase History class
class PurchaseHistory {
    private Stack<LinkedList<String>> history;

    public PurchaseHistory() {
        history = new Stack<>();
    }

    public void addToHistory(LinkedList<String> cart) {
        history.push(cart);
    }

    public LinkedList<String> undoLastPurchase() {
        if (!history.isEmpty()) {
            return history.pop();
        }
        return new LinkedList<>(); // Return an empty list if history is empty
    }

    public void viewHistory() {
        if (history.isEmpty()) {
            System.out.println("Purchase history is empty.");
        } else {
            System.out.println("Purchase History:");
            for (LinkedList<String> cart : history) {
                System.out.println(cart);
            }
        }
    }
}

// Customer Service class
class CustomerService {
    private Queue<String> serviceRequests;

    public CustomerService() {
        serviceRequests = new LinkedList<>();
    }

    public void addRequest(String request) {
        serviceRequests.add(request);
    }

    public void processRequest() {
        if (!serviceRequests.isEmpty()) {
            String request = serviceRequests.poll();
            System.out.println("Processing request: " + request);
        } else {
            System.out.println("No pending service requests.");
        }
    }

    public void viewRequests() {
        if (serviceRequests.isEmpty()) {
            System.out.println("No pending service requests.");
        } else {
            System.out.println("Pending Service Requests:");
            for (String request : serviceRequests) {
                System.out.println(request);
            }
        }
    }
}