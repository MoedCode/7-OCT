import React, { useState } from "react";
import { Link } from "react-router-dom";
import { useDispatch } from "react-redux";
import { useForm } from "react-hook-form";
import logo from "../assets/logo_v2.png";
import { TextInput, Loading, CustomButton } from "../components";

const Login = () => {
  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm({
    mode: "onChange",
  });

  const [errMsg, setErrMsg] = useState("");
  const [isSumbimitting, setIsSumbimitting] = useState(false);
  const dispatch = useDispatch();
  return (
    <div className="bg-bgColor w-full h-[100vh] flex items-center justify-center p-6">
      <div className="w-full md:w-2/3 h-fit lg:h-full 2xl:h-5/6 py-8 lg:py-0 flex bg-primary rounded-xl overflow-hidden shadow-xl">
        {/* Left section */}
        <div className="w-full lg:w-1/2 h-full p-10 2xl:px-20 flex flex-col justify-center">
          {/* LOGO  */}
          <div className="w-full flex gap-2 items-center mb-6">
            <img src={logo} alt="" className="logo" />
          </div>

          <p className="text-ascent-1 text-base font-semibold">
            Log in to your Account
          </p>
          <span className="text-sm mt-2 text-ascent-2">Welcome Back</span>
          <form className="py-8 flex flex-col gap-5">
            <TextInput
              name="email"
              placeholder="email@example.com"
              label="email"
              type="email"
              register={register("email", {
                required: "Email Address is required",
              })}
              styles="w-full rounded-full"
              labelStyle="ml-2"
              error={errors.email ? errors.email.message : ""}
            />

            <TextInput
              name="password"
              placeholder="Password"
              label="Password"
              type="password"
              labelStyle="ml-2"
              register={register("password", {
                required: " Password is required!",
              })}
              styles="w-full rounded-full"
              error={errors.password ? errors.password?.message : ""}
            />
            <Link
              to="/reset-password"
              className="text-right font-semibold text-red text-sm "
            >
              Forgot Password ?
            </Link>

            {errMsg?.message && (
              <span
                className={`text-sm ${
                  errMsg?.status == "failed"
                    ? "text-[#f64949fe"
                    : "text-[#2ba150fe]"
                } mt-0.5 `}
              >
                {errMsg?.message}
              </span>
            )}

            {isSumbimitting ? (
              <Loading />
            ) : (
              <CustomButton
                type="submit"
                containerStyles={`inline-flex justify-center rounded-md bg-red px-8 py-3 text-sm font-medium text-white outline-none`}
                title="Login"
              />
            )}
          </form>

          <p className="text-ascent-2 text-sm text-center">
            Don't have an account?
            <Link
              to="/register"
              className="text-[#db4b4b] font-semibold ml-2 cursor-pointer"
            >
              Create Account
            </Link>
          </p>
        </div>
        {/* right */}
        <div className=""></div>
      </div>
    </div>
  );
};

export default Login;
