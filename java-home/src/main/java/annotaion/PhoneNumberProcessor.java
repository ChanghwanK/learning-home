package annotaion;

import java.lang.annotation.Annotation;
import java.lang.reflect.Method;
import java.lang.reflect.Parameter;

public class PhoneNumberProcessor {
    public static void checker() throws NoSuchMethodException {
        System.out.println("Checking phone numbers...");
        Class<?> clazz = PhoneNumberBook.class;
//        Field[] fields = clazz.getDeclaredFields();
//        Annotation[] annotations = clazz.getDeclaredAnnotations();
        Method method = clazz.getDeclaredMethod("setPhoneNumber", String.class);
        Annotation[][] parameterAnnotations = method.getParameterAnnotations();
        for (Annotation[] parameterAnnotation : parameterAnnotations) {
            for (Annotation annotation : parameterAnnotation) {
                if (annotation instanceof PhoneNumberValidator) {
                    System.out.println("Phone number is valid.");
                    Parameter[] parameters = method.getParameters();
                    for (Parameter parameter : parameters) {
                        System.out.println(parameter);
                    }
                }
            }
        }
//        for (Annotation annotation : annotations) {
//            if (annotation instanceof PhoneNumberValidator) {
//                System.out.println("Found phone number validator");
//            }
//            if (annotation instanceof PhoneNumberPrinter) {
//                System.out.println("Found phone number printer");
//            }
//        }
//        for (Annotation annotation : clazz.getAnnotations()) {
//            if (annotation instanceof PhoneNumberValidator) {
//                PhoneNumberValidator validator = (PhoneNumberValidator) annotation;
//                System.out.println("Validator: " + validator.message());
//            }
//        }

//        for (Field field : fields) {
//            System.out.println(field);
//            if (field.isAnnotationPresent(PhoneNumberValidator.class)) {
//                PhoneNumberValidator validator = field.getAnnotation(PhoneNumberValidator.class);
//                System.out.println(validator.message());
//            }
//            if (field.isAnnotationPresent(PhoneNumberPrinter.class)) {
//                System.out.println();
//            }
        }
//    }
}
