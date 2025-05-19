import sqlite3

class TourStats:
    def __init__(self,db_path):
        self.connection = sqlite3.connect("data/database.db")
        self.cursor = self.connection.cursor()

    def get_tours_per_transport(self):
        try:
            self.cursor.execute("""
                SELECT 
                    CASE 
                        WHEN transportation IN (SELECT plate_number FROM Buses) THEN 'Bus'
                        ELSE transportation
                    END AS transport_type,
                    COUNT(*) AS count
                FROM TourFinancials
                GROUP BY transport_type
            """)
            results = self.cursor.fetchall()
            return results  # Λίστα με (transport_type, count)
        except Exception as e:
            print("Error getting tours per transport:", e)
            return []

    def get_average_people_per_tour(self):
        query = """
        SELECT AVG(participants) FROM TourFinancials
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else 0

    def get_most_profitable_tour(self):
        query = """
        SELECT tour_id, destination, profit_amount
        FROM TourFinancials
        ORDER BY profit_amount DESC
        LIMIT 1
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_tour_with_most_participants(self):
        query = """
        SELECT tour_id, destination, participants
        FROM TourFinancials
        ORDER BY participants DESC
        LIMIT 1
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()

    def get_profit_by_destination(self):
        query = """
        SELECT destination, SUM(profit_amount) AS total_profit
        FROM TourFinancials
        GROUP BY destination
        ORDER BY total_profit DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_average_km_per_tour(self):
        query = """
        SELECT AVG(km) FROM Tours
        WHERE status = 'Accepted' OR status = 'Completed'
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else 0
    
    def get_tours_per_bus(self):
        query = """
        SELECT transportation AS bus_plate, COUNT(*) AS total_tours
        FROM TourFinancials
        WHERE transportation NOT IN ('Airplain', 'Boat')
        GROUP BY transportation
        ORDER BY total_tours DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_average_total_cost_per_tour(self):
        query = """
        SELECT AVG(total_cost) FROM TourFinancials
        """
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        return result[0] if result else 0    
    
    def get_tour_count_per_driver(self):
        query = """
        SELECT driver, COUNT(*) AS total_tours
        FROM TourFinancials
        WHERE driver != ''
        GROUP BY driver
        ORDER BY total_tours DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_cost_stats_per_driver(self):
        query = """
        SELECT driver,
            SUM(driver_cost) AS total_driver_cost,
            AVG(driver_cost) AS avg_driver_cost
        FROM TourFinancials
        WHERE driver != ''
        GROUP BY driver
        ORDER BY total_driver_cost DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_driver_type_comparison(self):
        query = """
        SELECT d.type, COUNT(tf.tour_id) AS total_tours, AVG(tf.driver_cost) AS avg_cost
        FROM TourFinancials tf
        JOIN Drivers d ON tf.driver = d.tax_code
        GROUP BY d.type
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()    
    
    def get_driver_with_most_kilometers(self):
        query = """
        SELECT d.tax_code, d.f_name || ' ' || d.l_name AS name, SUM(t.km) AS total_km
        FROM TourFinancials tf
        JOIN Drivers d ON tf.driver = d.tax_code
        JOIN Tours t ON tf.tour_id = t.id
        GROUP BY d.tax_code
        ORDER BY total_km DESC
        LIMIT 1
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def get_cheapest_driver_per_day(self):
        query = """
        SELECT tax_code, f_name || ' ' || l_name AS name, MIN(salary / 22.0) AS cost_per_day
        FROM Drivers
        WHERE type = 'Permanent'
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()      
    
    def get_favorite_destinations(self):
        query = """
        SELECT destination, COUNT(*) AS times
        FROM TourFinancials
        GROUP BY destination
        ORDER BY times DESC
        LIMIT 3
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_tours_per_leader(self):
        query = """
        SELECT tl.id, tl.f_name || ' ' || tl.l_name AS name, COUNT(tf.tour_id) AS total_tours
        FROM TourFinancials tf
        JOIN TeamLeaders tl ON tf.guide = tl.id
        GROUP BY tl.id
        ORDER BY total_tours DESC
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def get_top_leader_by_tours(self):
        query = """
        SELECT tl.id, tl.f_name || ' ' || tl.l_name AS name, COUNT(tf.tour_id) AS total_tours
        FROM TourFinancials tf
        JOIN TeamLeaders tl ON tf.guide = tl.id
        GROUP BY tl.id
        ORDER BY total_tours DESC
        LIMIT 1
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def get_cheapest_leader_per_day(self):
        query = """
        SELECT id, f_name || ' ' || l_name AS name, ROUND(payment / 22.0, 2) AS cost_per_day
        FROM TeamLeaders
        ORDER BY cost_per_day ASC
        LIMIT 1
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()
    
    def get_top_destinations_by_leaders(self):
        query = """
        SELECT destination, COUNT(*) AS total
        FROM TourFinancials
        GROUP BY destination
        ORDER BY total DESC
        LIMIT 3
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    # ΕΚΤΟΣ κλάσης
if __name__ == "__main__":
    stats = TourStats("data/database.db")

    print("1. Πλήθος Tours ανά τύπο μεταφοράς:")#check
    print(stats.get_tours_per_transport())

    print("\n2. Μέσος αριθμός ατόμων ανά tour:")#check
    print(stats.get_average_people_per_tour())

    print("\n3. Πιο κερδοφόρο Tour:")#check
    print(stats.get_most_profitable_tour())

    print("\n4. Tour με τα περισσότερα άτομα:")#check
    print(stats.get_tour_with_most_participants())

    print("\n5. Κέρδος ανά προορισμό:")#---to look at---
    print(stats.get_profit_by_destination())

    print("\n6. Μέσος αριθμός χιλιομέτρων ανά tour:")
    print(stats.get_average_km_per_tour())

    print("\n7. Πλήθος Tours ανά Bus:")#check
    print(stats.get_tours_per_bus())

    print("\n8. Μέσος συνολικός κόστος ανά tour:")#check
    print(stats.get_average_total_cost_per_tour())

    print("\n9. Πλήθος Tours ανά οδηγό:")#check
    print(stats.get_tour_count_per_driver())

    print("\n10. Στατιστικά κόστους ανά οδηγό:")
    print(stats.get_cost_stats_per_driver())

    print("\n11. Σύγκριση τύπων οδηγών:")
    print(stats.get_driver_type_comparison())

    print("\n12. Οδηγός με τα περισσότερα χιλιόμετρα:")#chech
    print(stats.get_driver_with_most_kilometers())

    print("\n13. Φθηνότερος οδηγός ανά ημέρα:")#check
    print(stats.get_cheapest_driver_per_day())

    print("\n14. Αγαπημένοι προορισμοί:")#check
    print(stats.get_favorite_destinations())

    print("\n15. Πλήθος Tours ανά αρχηγό:")#ckeck
    print(stats.get_tours_per_leader())

    print("\n16. Κορυφαίος αρχηγός ανά Tours:")
    print(stats.get_top_leader_by_tours())#check

    print("\n17. Φθηνότερος αρχηγός ανά ημέρα:")
    print(stats.get_cheapest_leader_per_day())#check
    
    print("\n18. Κορυφαίοι προορισμοί ανά αρχηγό:")
    print(stats.get_top_destinations_by_leaders())#check
