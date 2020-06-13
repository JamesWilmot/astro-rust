#![allow(non_snake_case)]

#[macro_use]
extern crate astro;
extern crate assert_approx_eq;

use assert_approx_eq::assert_approx_eq;
use astro::*;

#[test]
fn hr_angl_dec_frm_hz() {
    // ha, dec, lat, alt, az
    // data generated from python utility utils/coords/hadec2altaz.py
    struct TestData(f64, f64, f64, f64, f64);
    
    //assert_approx_eq!(time::decimal_day(&day), data.5);
    let test_data = [
        TestData(0.0, 0.5235987755982988, 0.9334020839665674, 1.160993018426628, 0.0),
        TestData(0.7853981633974483, 0.20943951023931956, 
                -1.4046409820050365, -0.09077886258108678, 2.3738477459249516),
        TestData(0.8006889929741706, 1.4876175998362762, -0.8810637263164147,
                -0.8211672541063436, 3.053950833397557),
    ];
    
    for datum in test_data.iter() {
        // pub fn hr_angl_frm_hz(az: f64, alt: f64, observer_lat: f64) -> f64
        assert_approx_eq!(coords::hr_angl_frm_hz(datum.4, datum.3, datum.2), datum.0);

        // pub fn dec_frm_hz(az: f64, alt: f64, observer_lat: f64) -> f64
        assert_approx_eq!(coords::dec_frm_hz(datum.4, datum.3, datum.2), datum.1);
    }
}
