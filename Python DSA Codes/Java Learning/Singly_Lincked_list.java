import java.util.*;

class Node {
    int data;
    Node next;

    Node(int data) {
        this.data = data;
        this.next = null;
    }
}

class Singly_Lincked_list {
    Node head;

    Singly_Lincked_list() {
        head = null;
    }

    void insert_end(int data) {
        Node temp = new Node(data);

        if (head == null) {
            head = temp;
        } else {
            Node t1 = head;
            while (t1.next != null) {
                t1 = t1.next;
            }
            t1.next = temp;
        }
    }

    void print() {
        Node t1 = head;
        while (t1 != null) {
            System.out.println(t1.data);
            t1 = t1.next;
        }

    }

    public static void main(String[] args) {
        Singly_Lincked_list obj = new Singly_Lincked_list();
        obj.insert_end(10);
        obj.insert_end(20);
        obj.insert_end(30);
        obj.print();
    }
}