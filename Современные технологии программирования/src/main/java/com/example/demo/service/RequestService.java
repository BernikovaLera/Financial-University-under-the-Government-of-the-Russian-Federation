package com.example.demo.service;

import java.security.Principal;
import java.util.List;

import com.example.demo.domain.Request;
import com.example.demo.domain.User;
import com.example.demo.repos.RequestRepo;
import com.example.demo.repos.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class RequestService {
    @Autowired
    private RequestRepo repo;

    private final UserRepository userRepository;

    public List<Request> listAll(String keyword) {
        if (keyword != null) {
            return repo.search(keyword);
        }
        return repo.findAll();
    }

    public User getUserByPrincipal(Principal principal) {
        if (principal == null) return new User();
        return userRepository.findByEmail(principal.getName());
    }

    public void save(Request request) {
        repo.save(request);
    }

    public Request get(Long id) {
        return repo.findById(id).get();
    }

    public void delete(Long id) {
        repo.deleteById(id);
    }

}
