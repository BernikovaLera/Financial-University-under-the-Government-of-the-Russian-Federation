package com.example.demo.repos;

import java.util.List;

import com.example.demo.domain.Request;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

public interface RequestRepo extends JpaRepository<Request, Long> {
    @Query("SELECT p FROM Request p WHERE LOWER(CONCAT(p.id, ' ', " +
            "p.title, ' ', p.createdDate, ' ', p.modifiedDate, ' ', " +
            "p.status, ' ', p.description)) " +
            "LIKE LOWER(CONCAT('%', ?1, '%'))")
    List<Request> search(String keyword);
}
