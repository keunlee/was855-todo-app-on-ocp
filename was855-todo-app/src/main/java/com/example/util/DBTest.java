package com.example.util;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DBTest {
    public static void main( String args[] ) {
        String jdbcClassname="org.postgresql.Driver";
        String url="jdbc:postgresql://127.0.0.1:5432/testdb";
        String user="postgres";
        String password="postgres";

        PreparedStatement pstmt = null;
        ResultSet rset = null;
        boolean found = false;
        Connection connection = null;

        try {
            Class.forName(jdbcClassname);
            connection = DriverManager.getConnection(url,user,password);
            if ( connection != null) {
                System.out.println("DB Connected");
            } else {
                System.out.println("DB Failed");
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}
