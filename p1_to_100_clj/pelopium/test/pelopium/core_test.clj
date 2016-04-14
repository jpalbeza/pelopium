(ns pelopium.core-test
  (:require [clojure.test :refer :all]
            [pelopium.core :refer :all]))

(deftest p1-trigo-test
  (testing "p1-trigo"
    (is (= (p1-trigo) 233168))))


