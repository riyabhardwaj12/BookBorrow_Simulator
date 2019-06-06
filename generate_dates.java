import java.util.*;
class dates {
    public static int randBetween(int start, int end) {
        //int random = (int )(Math.random() * end + start);
        Random r = new Random();
        int result = -1;
        try {
            result = r.nextInt(end - start) + start;
        } catch (Exception e) {
            System.out.println(e);
        }
        //return start + (int)Math.round(Math.random() * (end - start));
        return result;
    }
   public static void main(String[]args)
   {
       Scanner sc=new Scanner(System.in);
        int arr[] = new int[24];
        int j = 0;

        for (int i = 7; i <= 30; i++, j++) {
            arr[j] = i;
        }
        //SimpleDateFormat dfDateTime  = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss", Locale.getDefault());
       
       int month = randBetween(1, 12);

               // System.out.println(month);

                int day = 1;
                int day2 = 8;
                int month2 = month, year2;
                int year = randBetween(1900, 2019);

               // System.out.println(day + " " + day2 + " " + month2 + " " + year);

                year2 = year;
                int dur = randBetween(0, 23);


                int day3, month3, year3;
                int are[] = {-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7};
                int durre = randBetween(0, 11);
                //System.out.println(year2 + " " + dur);

                if (month == 4 || month == 6 || month == 9 || month == 11) {
                    //System.out.println("hey");
                    day = randBetween(1, 30);
                    day2 += arr[dur];

                    if (day2 > 30) {
                        day2 = day2 - 30;
                        month2++;
                    }
                    if (month2 > 12) {
                        month2 = 1;
                        year2++;
                    }
                  //  System.out.println("hey");

                } else if (month == 2) {
                   // System.out.println("hey2");
                    day = randBetween(1, 28);
                    day2 += arr[dur];
                    if (day2 > 28) {
                        day2 = day2 - 28;
                        month2++;
                    }
                    if (month2 > 12) {
                        month2 = 1;
                        year2++;
                    }
                   // System.out.println("hey2");
                } else {
                    //System.out.println("hey3");
                    day = randBetween(1, 31);
                    day2 += arr[dur];
                    if (day2 > 31) {
                        day2 = day2 - 31;
                        month2++;
                    }
                    if (month2 > 12) {
                        month2 = 1;
                        year2++;
                    }
                   // System.out.println("hey3");
                }
                //System.out.println("hey4");
               // System.out.println(day + "-" + month + "-" + year);
               // System.out.println(day2 + "-" + month2 + "-" + year2);

                day3 = day2 + are[durre];
                month3 = month2;
                year3 = year2;
               // System.out.println(month3 + "-" + day3 + "-" + year3);
                if (month2 == 1) {
                    if (day3 < 1) {
                        day3 = 31;
                        month3 = 12;
                        year3 = year2 - 1;
                    }
                    if (day3 > 31) {
                        day3 = 1;
                        month3 = 2;
                        year3 = year2 + 1;
                    }
                }
                if (month2 == 2) {
                    if (day3 < 1) {
                        day3 = 31;
                        month3 = 1;
                        year3 = year2;
                    }
                    if (day3 > 28) {
                        day3 = 1;
                        month3 = 3;
                        year3 = year2;
                    }
                }
                if (month2 == 3) {
                    if (day3 < 1) {
                        day3 = 28;
                        month3 = 2;
                        year3 = year2;
                    }
                    if (day3 > 31) {
                        day3 = 1;
                        month3 = 4;
                        year3 = year2;
                    }
                }
                if (month2 == 4 || month2 == 6 || month2 == 9 || month2 == 11) {
                    if (day3 < 1) {
                        day3 = 31;
                        month3 = month2 - 1;
                        year3 = year2;
                    }
                    if (day3 > 31) {
                        day3 = 1;
                        month3 = month2 + 1;
                        year3 = year2;
                    }
                }
                if (month2 == 5 || month2 == 7 || month2 == 8 || month2 == 10) {
                    if (day3 < 1) {
                        day3 = 30;
                        month3 = month2 - 1;
                        year3 = year2;
                    }
                    if (day3 > 31) {
                        day3 = 1;
                        month3 = month2 + 1;
                        year3 = year2;
                    }
                }
                if (month2 == 12) {
                    if (day3 < 1) {
                        day3 = 30;
                        month3 = 11;
                        year3 = year2;
                    }
                    if (day3 > 31) {
                        day3 = 1;
                        month3 = 1;
                        year3 = year2 + 1;
                    }
                }
               // System.out.println(month3 + "-" + day3 + "-" + year3);
                String dat = String.valueOf(day3) + "-" + String.valueOf(month3) + "-" + String.valueOf(year3);
               System.out.println(dat);//actual ret date
                dat = String.valueOf(day2) + "-" + String.valueOf(month2) + "-" + String.valueOf(year2);
               System.out.println(dat);//date claim to ret
                dat = String.valueOf(day) + "-" + String.valueOf(month) + "-" + String.valueOf(year);
                System.out.println(dat);//date of borrow

        }
    }
