#!/bin/bash

cat NP_MTurk_dec_f1.txt NP_MTurk_dec_f2.txt NP_MTurk_dec_f3.txt NP_MTurk_dec_f4.txt NP_MTurk_dec_f5.txt > Negative_fake_all.txt

wc Negative_fake_all.txt

cat NP_Web_truth_f1.txt NP_Web_truth_f2.txt NP_Web_truth_f3.txt NP_Web_truth_f4.txt NP_Web_truth_f5.txt > Negative_real_all.txt

wc Negative_real_all.txt

cat PP_MTurk_dec_f1.txt PP_MTurk_dec_f2.txt PP_MTurk_dec_f3.txt PP_MTurk_dec_f4.txt PP_MTurk_dec_f5.txt > Positive_fake_all.txt

wc Positive_fake_all.txt

cat PP_TripAdvisor_truth_f1.txt PP_TripAdvisor_truth_f2.txt PP_TripAdvisor_truth_f3.txt PP_TripAdvisor_truth_f4.txt PP_TripAdvisor_truth_f5.txt > Positive_real_all.txt

wc Positive_real_all.txt
