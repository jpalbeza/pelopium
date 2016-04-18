(ns pelopium.core-test
  (:require [clojure.test :refer :all]
            [pelopium.core :refer :all]))

(deftest p1-trigo-test
  (testing "p1-trigo-v1"
    (is (= (p1-trigo-v1) 233168))))

(deftest p1-trigo-v2-test
  (testing "p1-trigo-v2"
    (is (= (p1-trigo-v2 1000) 233168))))

(deftest p1-v1
  (testing "p2-v1"
    (is (= (p2-v1 (partial even?) 4000000)) 4613732)))

(deftest jp-iter-test
  (testing "jp-iter"
    (is (and
          (= (take 5 (jp-iter #(* 2 %) 1)) [1 2 4 8 16])
          (= (take 100 (jp-iter inc 0)) (take 100 (range)))
          (= (take 9 (jp-iter #(inc (mod % 3)) 1)) (take 9 (cycle [1 2 3])))))))

(deftest jp-interleave-test
  (testing "jp-interleave"
    (is (and
          (= (jp-interleave [:a :b :c] [1 2 3]) {:a 1, :b 2, :c 3})
          (= (jp-interleave [1 2 3 4] ["one" "two" "three"]) {1 "one", 2 "two", 3 "three"})
          (= (jp-interleave [:foo :bar] ["foo" "bar" "baz"]) {:foo "foo", :bar "bar"})))))

(deftest jp-juxt-test
  (testing "jp-juxt"
    (is (and
          (= [21 6 1] ((jp-juxt + max min) 2 3 5 1 6 4))
          (= ["HELLO" 5] ((jp-juxt #(.toUpperCase %) count) "hello"))
          (= [2 6 4] ((jp-juxt :a :c :b) {:a 2, :b 4, :c 6, :d 8 :e 10}))))))
