// swift-tools-version: 5.9
// The swift-tools-version declares the minimum version of Swift required to build this package.

import PackageDescription

let package = Package(
    name: "PhotoOCRApp",
    platforms: [
        .iOS(.v17)
    ],
    products: [
        .library(
            name: "PhotoOCRApp",
            targets: ["PhotoOCRApp"]),
    ],
    dependencies: [
        // No external dependencies required - uses Apple's built-in frameworks
    ],
    targets: [
        .target(
            name: "PhotoOCRApp",
            dependencies: [],
            path: "PhotoOCRApp"),
        .testTarget(
            name: "PhotoOCRAppTests",
            dependencies: ["PhotoOCRApp"]),
    ]
)